from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "user"

    user_id = Column(String(36), primary_key=True, nullable=False)  # Length set to 36 for UUIDs
    username = Column(String(50), nullable=False)  # Adjust length as needed
    password_hash = Column(String(128), nullable=False)  # Adjust length to suit hashed passwords
    email = Column(String(100), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    role = Column(String(20), nullable=False)  # Example length for roles like 'admin' or 'user'
    profile_picture = Column(String(255), nullable=False)  # Adjust length for URLs or file paths
    bio = Column(String(500), nullable=False)  # Length for user bios
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class SportType(Base):
    __tablename__ = "sporttype"

    sport_type_id = Column(String(36), primary_key=True, nullable=False)  # Length for UUID or similar unique ID
    sport_name = Column(String(100), nullable=False)  # Adjust length for sport names
    description = Column(String(500), nullable=False)  # Adjust length for descriptions
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class Exercise(Base):
    __tablename__ = "exercise"

    exercise_id = Column(String(36), primary_key=True, nullable=False)  # Length for unique ID (UUID or similar)
    sport_type_id = Column(
        String(36), ForeignKey("sporttype.sport_type_id"), nullable=False  # Matches the length in the referenced table
    )
    exercise_name = Column(String(100), nullable=False)  # Adjust length for exercise names
    description = Column(String(500), nullable=False)  # Length for exercise descriptions
    video_url = Column(String(255), nullable=False)  # Length for URLs
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class Routine(Base):
    __tablename__ = "routine"

    routine_id = Column(String(36), primary_key=True, nullable=False)  # Length for unique ID (UUID or similar)
    trainer_id = Column(String(36), ForeignKey("user.user_id"), nullable=False)  # Matches length in the referenced `user` table
    routine_name = Column(String(100), nullable=False)  # Adjust length for routine names
    description = Column(String(500), nullable=False)  # Length for detailed descriptions
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class RoutineExercise(Base):
    __tablename__ = "routineexercise"

    routine_exercise_id = Column(String(36), primary_key=True, nullable=False)  # Length for unique ID (UUID or similar)
    routine_id = Column(String(36), ForeignKey("routine.routine_id"), nullable=False)  # Matches length in the `routine` table
    exercise_id = Column(String(36), ForeignKey("exercise.exercise_id"), nullable=False)  # Matches length in the `exercise` table
    sets = Column(Integer, nullable=False)  # Number of sets
    repetitions = Column(Integer, nullable=False)  # Number of repetitions
    duration = Column(Integer, nullable=False)  # Duration in seconds or minutes (adjust per app logic)
    created_at = Column(DateTime, nullable=False)  # Timestamp for record creation

class Workout(Base):
    __tablename__ = "workout"

    workout_id = Column(String(36), primary_key=True, nullable=False)  # Length for unique ID (UUID or similar)
    trainee_id = Column(String(36), ForeignKey("user.user_id"), nullable=False)  # Matches the length of `user_id` in the `user` table
    routine_id = Column(String(36), ForeignKey("routine.routine_id"), nullable=False)  # Matches the length of `routine_id` in the `routine` table
    workout_date = Column(DateTime, nullable=False)  # Date and time of the workout
    duration = Column(Integer, nullable=False)  # Duration of the workout (e.g., in minutes)
    created_at = Column(DateTime, nullable=False)  # Timestamp for record creation
    updated_at = Column(DateTime, nullable=False)  # Timestamp for the last update

class WorkoutExercise(Base):
    __tablename__ = "workoutexercise"

    workout_exercise_id = Column(String(36), primary_key=True, nullable=False)  # Length for unique ID (UUID or similar)
    workout_id = Column(String(36), ForeignKey("workout.workout_id"), nullable=False)  # Matches the length of `workout_id` in the `workout` table
    routine_exercise_id = Column(String(36), ForeignKey("routineexercise.routine_exercise_id"), nullable=False)  # Matches the length of `routine_exercise_id` in the `routine_exercise` table
    sets_completed = Column(Integer, nullable=False)  # Number of sets completed
    repetitions_completed = Column(Integer, nullable=False)  # Number of repetitions completed
    created_at = Column(DateTime, nullable=False)  # Timestamp for record creation

class Follower(Base):
    __tablename__ = "follower"

    follower_id = Column(String(36), primary_key=True, nullable=False)  # Length for unique ID (UUID or similar)
    influencer_id = Column(String(36), ForeignKey("user.user_id"), nullable=False)  # Matches the length of `user_id` in the `user` table
    trainee_id = Column(String(36), ForeignKey("user.user_id"), nullable=False)  # Matches the length of `user_id` in the `user` table
    created_at = Column(DateTime, nullable=False)  # Timestamp for record creation