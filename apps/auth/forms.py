from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SignUpForm(FlaskForm):
    
    toyname = StringField(
        "장난감이름",
        validators=[
            DataRequired(message="장난감이름은 필수입니다.")
        ],
    )

    age = StringField(
        "연령",
        validators=[
            DataRequired(message="가능한 연령를 입력해주세요.")
        ],
    )
    
    components = StringField(
        "구성품",
        validators=[
            DataRequired(message="구성품에 대해 입력해주세요.")
        ],
    )

    explain = StringField(
        "장난감 설명",
        validators=[
            DataRequired(message="장난감에 대한 간단한 설명을 입력해주세요."),
            Length(max=20, message="20문자 이내로 입력해 주세요.")
        ],
    )
    
    rental = StringField(
        "대여 여부",
        validators=[
            DataRequired(message="대여 여부를 입력해주세요.")
        ]
    )
    
    submit = SubmitField("신규 등록") 