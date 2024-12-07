from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):

    user_id: str

    username: str

    password_hash: str

    email: str

    first_name: str

    last_name: str

    role: str

    profile_picture: str

    bio: str

    created_at: datetime

    updated_at: datetime

    class Config:
        orm_mode = True

class UserCreate(UserSchema):
    pass

class SportTypeSchema(BaseModel):

    sport_type_id: str

    sport_name: str

    description: str

    created_at: datetime

    updated_at: datetime

    class Config:
        orm_mode = True

class SportTypeCreate(SportTypeSchema):
    pass

class ExerciseSchema(BaseModel):

    exercise_id: str

    sport_type_id: str

    exercise_name: str

    description: str

    video_url: str

    created_at: datetime

    updated_at: datetime

    class Config:
        orm_mode = True

class ExerciseCreate(ExerciseSchema):
    pass

class RoutineSchema(BaseModel):

    routine_id: str

    trainer_id: str

    routine_name: str

    description: str

    created_at: datetime

    updated_at: datetime

    class Config:
        orm_mode = True

class RoutineCreate(RoutineSchema):
    pass

class RoutineExerciseSchema(BaseModel):

    routine_exercise_id: str

    routine_id: str

    exercise_id: str

    sets: int

    repetitions: int

    duration: int

    created_at: datetime

    class Config:
        orm_mode = True

class RoutineExerciseCreate(RoutineExerciseSchema):
    pass

class WorkoutSchema(BaseModel):

    workout_id: str

    trainee_id: str

    routine_id: str

    workout_date: str

    duration: int

    created_at: datetime

    updated_at: datetime

    class Config:
        orm_mode = True

class WorkoutCreate(WorkoutSchema):
    pass

class WorkoutExerciseSchema(BaseModel):

    workout_exercise_id: str

    workout_id: str

    routine_exercise_id: str

    sets_completed: int

    repetitions_completed: int

    created_at: datetime

    class Config:
        orm_mode = True

class WorkoutExerciseCreate(WorkoutExerciseSchema):
    pass


class FollowerSchema(BaseModel):

    follower_id: str

    influencer_id: str

    trainee_id: str

    created_at: datetime

    class Config:
        orm_mode = True

class FollowerCreate(FollowerSchema):
    pass

