"""Presentation layer entry point. Menus will be added in Hito 2."""
from ..persistence.connection import get_connection, init_db


def main() -> None:
    conn = get_connection()
    init_db(conn)
    print("Viajes Aventura: base de datos lista.")
    conn.close()


if __name__ == "__main__":
    main()
