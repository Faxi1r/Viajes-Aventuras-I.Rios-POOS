"""AuthService and DataValidator skeletons (to be implemented in Hito 2)."""
from .models import Destination, Reservation, TourPackage, User


class DataValidator:
    def validate_user(self, user: User) -> bool:
        raise NotImplementedError

    def validate_destination(self, destination: Destination) -> bool:
        raise NotImplementedError

    def validate_package(self, package: TourPackage) -> bool:
        raise NotImplementedError

    def validate_reservation(self, reservation: Reservation) -> bool:
        raise NotImplementedError


class AuthService:
    def __init__(self, validator: DataValidator) -> None:
        self.validator = validator

    def register_user(self, user: User) -> bool:
        raise NotImplementedError

    def login(self, email: str, password: str) -> bool:
        raise NotImplementedError

    def verify_credentials(self, email: str, password: str) -> bool:
        raise NotImplementedError
