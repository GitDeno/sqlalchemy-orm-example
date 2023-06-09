from models import Base, User
from session import session


def main():
    # Create all tables
    Base.metadata.create_all()

    # Create a new user
    user = User(
        first_name="John",
        last_name="Doe",
        user_name="johndoe",
        email="john.doe@gmail.com"
    )

    session.add(user)
    session.commit()


if __name__ == "__main__":
    main()
