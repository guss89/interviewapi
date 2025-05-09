from sqlalchemy.orm import Session
from collections import defaultdict
from sqlalchemy import join, select

#schema
from app.schemas.interviewQuestion import InterviewQuestionUpdate, InterviewQuestionCreate, InterviewQuestionOut

#Models
from app.models.interviewQuestion import InterviewQuestion
from app.models.store import Store
from app.models.interview import Interview
from app.models.question import Question
from app.models.catAnswer import CatAnswer

from app.models.client import Client
from app.models.waiter import Waiter
from app.models.hostess import Hostess
from app.models.answer import Answer
from app.models.comments import Comments

def get_all_interviewQuestion(db:Session):
    return db.query(InterviewQuestion).all()

def get_all_intervireQuestion_id(db:Session, interview_id: int):
    interviews = db.query(InterviewQuestion).filter(InterviewQuestion.interview_id == interview_id).all()
    if interviews:
       return interviews
    else:
        return None
    
def create_interviewQuestion(db:Session, interviewQuestion: InterviewQuestionCreate):
    db_interview = InterviewQuestion(**interviewQuestion.dict())
    db.add(db_interview)
    db.commit()
    db.refresh(db_interview)
    return db_interview

def update_interviewQuestion(db:Session, interviewQuestion_id: int ,interviewQuestion_data: InterviewQuestionUpdate ):
    db_interviewQuestion = db.query(InterviewQuestion).filter(InterviewQuestion.id == interviewQuestion_id).first()
    if not db_interviewQuestion:
        return None
    
    for key, value in interviewQuestion_data.dict(exclude_unset=True).items():
        setattr(db_interviewQuestion, key, value)

    db.commit()
    db.refresh(db_interviewQuestion)
    return db_interviewQuestion

def delete_interviewQuestion(db:Session, interviewQuestion_id:int):
    interview = db.query(InterviewQuestion).filter(InterviewQuestion.id == interviewQuestion_id).first()
    if not interview:
        return None
    db.delete(interview)
    db.commit()
    return {"detail":"Interview deleted successfully"}

def get_interviews(db: Session, interview_id: int) -> dict:
    # Obtener nombre del store e interview
    store = db.query(Store.name.label("store"), Store.id.label("store_id")) \
        .join(Store, InterviewQuestion.store) \
        .filter(InterviewQuestion.interview_id == interview_id) \
        .first()

    interview = db.query(Interview.name.label("interview"), Interview.id.label("interview_id")) \
        .join(Interview, InterviewQuestion.interview) \
        .filter(InterviewQuestion.interview_id == interview_id) \
        .first()

    # Obtener las preguntas con tipo incluido
    question_query = db.query(
        InterviewQuestion.id.label("interview_question_id"),
        Question.id.label('question_id'),
        Question.description.label("question"),
        Question.question_type.label("question_type"),
    ).join(Question, InterviewQuestion.question) \
     .filter(InterviewQuestion.interview_id == interview_id)

    questions_data = db.execute(question_query).all()

    # Obtener todas las opciones y agruparlas por option_type
    cat_answers = db.query(CatAnswer).all()
    options_by_type = defaultdict(list)
    for option in cat_answers:
        options_by_type[option.option_type].append({
            "id": option.id,
            "description": option.description
        })

    # Construir la lista de preguntas con sus opciones correspondientes por tipo
    questions = []
    for row in questions_data:
        questions.append({
            "interview_question_id": row.interview_question_id,
            "question_id": row.question_id,
            "question": row.question,
            "question_type": row.question_type,
            "options": options_by_type.get(row.question_type, [])
        })

    return {
        "store_id": store.store_id,
        "store": store.store if store else None,
        "interview_id":interview.interview_id,
        "interview": interview.interview if interview else None,
        "questions": questions
    }

def save_interview_data(db: Session, data: dict):
    try:
        # 1. Buscar o crear cliente
        client = Client(name=data["client"]["name"], phone=data["client"]["phone"])
        db.add(client)
        db.flush()  # Para obtener client.id

        # 2. Buscar mesero (puedes hacer lógica más robusta si es necesario)
        waiter = db.query(Waiter).filter_by(name=data["waiter"]).first()
        if not waiter:
            waiter = Waiter(name=data["waiter"], store_id=data["store_id"])
            db.add(waiter)
            db.flush()

        # 3. Buscar hostess
        hostess = db.query(Hostess).get(data["hostess"])
        if not hostess:
            raise ValueError("Hostess ID inválido")


        # 4. Agregar respuestas
        for answer_data in data["answers"]:
            answer = Answer(
                waiter_id = waiter.id,
                hostess_id = data["hostess"],
                interview_question_id=answer_data["interview_question_id"],
                cat_answer_id=answer_data["cat_answer_id"]
            )
            db.add(answer)

        # 5. Agregar comentario
        comment = Comments( description=data["comments"])
        db.add(comment)

        # 6. Confirmar transacción
        db.commit()
        return {"detail":"Interview save successfully"}
    except Exception as e:
        db.rollback()  # Revierte los cambios si algo falla
        return {"detail":f"Error al guardar encuesta: {e}"}