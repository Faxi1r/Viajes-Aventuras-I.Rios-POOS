"""Domain entities from the UML class diagram (business layer)."""
from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class User:
    id: int | None
    name: str
    email: str
    password_hash: str
    role: str = "client"


@dataclass
class Destination:
    id: int | None
    name: str
    description: str
    location: str
    status: str = "active"


@dataclass
class PackageDestination:
    destination_id: int
    associated_cost: Decimal

    def get_cost(self) -> Decimal:
        return self.associated_cost


@dataclass
class TourPackage:
    id: int | None
    name: str
    description: str
    start_date: date
    end_date: date
    available: bool = True


@dataclass
class Reservation:
    id: int | None
    user_id: int
    package_id: int
    reserved_at: date
    people_count: int
    total_price: Decimal
    status: str = "pending"
