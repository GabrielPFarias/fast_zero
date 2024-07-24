from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='Gabriel', email='gabr@iel.com', password='123')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'gabr@iel.com'))

    assert result.username == 'Gabriel'
