from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.dependency import get_db
from app.services.quiz_service import QuizService
from app.schemas.schema import QuizTopicCreateRequest, QuizTopicResponse, QuizTopicResponseWrapper, QuizTopicUpdateRequest

router = APIRouter(tags=['Quiz'])
quiz_service = QuizService()

######################
# Create Quiz Topic Route
######################
@router.post("/create_quiz_topic", response_model=QuizTopicResponseWrapper)
def create_quiz_topic(quiz_topic: QuizTopicCreateRequest, db: Session = Depends(get_db)):
    try:
        created_topics = quiz_service.create_quiz_topic(db, quiz_topic)
        response = QuizTopicResponseWrapper(
            topics=[
                QuizTopicResponse(
                    id=topic.id,
                    name=topic.name,
                    is_active=topic.is_active
                )
                for topic in created_topics
            ],
            message="Quiz topics created successfully"
        )
        return response
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error creating quiz topics: {str(e)}"
        )

######################
# Get All Quiz Topics Route
######################
@router.get("/get_all_quiz_topics", response_model=QuizTopicResponseWrapper)
def get_all_quiz_topics(db: Session = Depends(get_db)):
    try:
        topics = quiz_service.get_all_quiz_topics(db)
        response = QuizTopicResponseWrapper(
            topics=[
                QuizTopicResponse(
                    id=topic.id,
                    name=topic.name,
                    is_active=topic.is_active
                )
                for topic in topics
            ]
        )
        return response
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching quiz topics: {str(e)}"
        )
    
######################
# Update Quiz Topic Route
######################
@router.put("/update_quiz_topic", response_model=QuizTopicResponseWrapper)
def update_quiz_topic(quiz_topic: QuizTopicUpdateRequest, db: Session = Depends(get_db)):
    try:
        updated_topic = quiz_service.update_quiz_topic(db, quiz_topic)
        response = QuizTopicResponseWrapper(
            topics=[
                QuizTopicResponse(
                    id=updated_topic.id,
                    name=updated_topic.name,
                    is_active=updated_topic.is_active
                )
            ],
            message="Quiz topic updated successfully"
        )
        return response
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error updating quiz topics: {str(e)}"
        )

#######################
# Delete Quiz Topic Route
########################
@router.delete("/delete_quiz_topic/{topic_id}", response_model=QuizTopicResponseWrapper)
def delete_quiz_topic(topic_id: int, db: Session = Depends(get_db)):
    try:
        delete_quiz_topic = quiz_service.delete_quiz_topic(db, topic_id)
        response = QuizTopicResponseWrapper(
            topics=[],
            message=delete_quiz_topic["message"]
        )
        return response
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error deleting quiz topic: {str(e)}"
        )