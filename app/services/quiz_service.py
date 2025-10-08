from app.models.model import QuizTopic
from sqlalchemy.orm import Session
from fastapi import HTTPException
# from app.schemas.schema import QuizTopicCreate, QuizTopicResponse


class QuizService:
    def create_quiz_topic(self, db: Session, topic):
        topic_names = topic.name

        existing = (
            db.query(QuizTopic.name)
            .filter(QuizTopic.name.in_(topic_names))
            .all()
        )

        if existing:
            existing_names = [t.name for t in existing]
            raise HTTPException(
                status_code=400,
                detail=f"Quiz topic(s) already exist: {', '.join(existing_names)}"
            )

        db.bulk_insert_mappings(
            QuizTopic,
            [{"name": name} for name in topic_names]
        )
        db.commit()

        created_topics = db.query(QuizTopic).filter(QuizTopic.name.in_(topic_names)).all()
        return created_topics


    def get_all_quiz_topics(self, db:Session):
        topics = db.query(QuizTopic).all()
        return topics

    def update_quiz_topic(self, db:Session, quiz_topic):
        topic = db.query(QuizTopic).filter(QuizTopic.id == quiz_topic.id).first()
        if not topic:
            raise HTTPException(status_code=404, detail="Quiz topic not found")

        topic.name = quiz_topic.name
        topic.is_active = quiz_topic.is_active
        db.commit()
        db.refresh(topic)
        return topic
    
    def delete_quiz_topic(self, db:Session, topic_id: int):
        topic = db.query(QuizTopic).filter(QuizTopic.id == topic_id).first()
        if not topic:
            raise HTTPException(status_code=404, detail="Quiz topic not found")

        db.delete(topic)
        db.commit()
        return {"message": "Quiz topic deleted successfully"}