from lifevector.db.connections import Database
from lifevector.models.roles import Role


class RoleRepository:
    def __init__(self):
        self.db_manager = Database()

    def activate(self, id):
        """This function can be used to activate an existing role from the LifeVector database if not already"""

        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Activate role
        cur.execute("UPDATE roles SET is_active = ? WHERE id = ?", (1, str(id)))

        # Commit and close connection
        con.commit()
        con.close()

    def add_role(self, role: Role) -> None:
        """This function can be used to add a new role to the LifeVector database"""

        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Add role to the database
        cur.execute(
            "INSERT INTO roles (name, description, sort_order) VALUES (?, ?, ?)",
            (role.name, role.description, role.sort_order),
        )

        # Commit and close connection
        con.commit()
        con.close()

    def count(self) -> int:
        """This function returns the total number of roles in the LifeVector database."""
        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Retrive number of roles in the database
        row = cur.execute("SELECT COUNT(*) FROM roles").fetchone()
        count = int(row[0])

        # Close connection
        con.close()

        # Return number of roles in the database
        return count

    def deactivate(self, id):
        """This function can be used to deactivate an existing role from the LifeVector database if not already"""

        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Deactivate role
        cur.execute("UPDATE roles SET is_active = ? WHERE id = ?", (0, str(id)))

        # Commit and close connection
        con.commit()
        con.close()

    def get_all_roles(self, status: str = "all") -> list[Role] | None:
        """This function returns a list of roles present in the LifeVector database that match the provided status. If no status is given or the caller provides an invalid status then it returns all of the roles"""

        # Determine the right SQL query
        if status == "active":
            query = "SELECT * FROM roles WHERE is_active = 1 ORDER BY sort_order ASC"
        elif status == "inactive":
            query = "SELECT * FROM roles WHERE is_active = 0 ORDER BY sort_order ASC"
        else:
            query = "SELECT * FROM roles ORDER BY sort_order ASC"

        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Retrive data for specified roles
        rows = cur.execute(query).fetchall()

        # Commit and close connection
        con.commit()
        con.close()

        # Validate result
        if not rows:
            return None

        roles = []

        # Fill the list with roles
        for row in rows:
            roles.append(
                Role(
                    row[1],
                    row[3],
                    description=row[2],
                    is_active=bool(row[4]),
                    id=row[0],
                )
            )

        return roles

    def get_first_sort_order(self) -> str | None:
        """This function returns the sort_order of the orderwise first role in the LifeVector database"""

        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Retreive sort order roles
        row = cur.execute("SELECT MIN(sort_order) FROM roles").fetchone()

        # Commit and close connection
        con.commit()
        con.close()

        # Validate data
        if not row:
            return None

        return row[0]

    def get_last_sort_order(self) -> str | None:
        """This function returns the sort_order of the orderwise last role in the LifeVector database"""

        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Retreive sort order roles
        row = cur.execute("SELECT MAX(sort_order) FROM roles").fetchone()

        # Commit and close connection
        con.commit()
        con.close()

        # Validate data
        if not row:
            return None

        return row[0]

    def get_role(self, id: int) -> Role | None:
        """This function returns a role object from the LifeVector database which matches the provided id"""

        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Retrive role's data
        row = cur.execute("SELECT * FROM roles WHERE id = ?", (str(id),)).fetchone()

        # Commit and close connection
        con.commit()
        con.close()

        # Validate result
        if not row:
            return None

        # Create a role object and return  it
        return Role(
            row[1], row[3], description=row[2], is_active=bool(row[4]), id=row[0]
        )

    def remove_all_roles(self, status: str = "inactive") -> None:
        """This function deletes all of the roles present in the LifeVector database that match the provided status. If no status is given or the caller provides an invalid status then it deletes all of the inactive roles"""

        # Determine the right SQL query
        if status == "active":
            query = "DELETE FROM roles WHERE is_active = 1"
        elif status == "all":
            query = "DELETE FROM roles"
        else:
            query = "DELETE FROM roles WHERE is_active = 0"

        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Remove all specified roles
        cur.execute(query)

        # Commit and close connection
        con.commit()
        con.close()

    def remove_role(self, id: int) -> None:
        """This function deletes a role from the LifeVector database if it exists"""
        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Remove role
        cur.execute("DELETE FROM roles WHERE id = ?", (str(id),))

        # Commit and close connection
        con.commit()
        con.close()

    def set_sort_order(self, id: int, key: str) -> None:
        """This function can be used to update/modify the sort_order atribute of an existing role from the LifeVector database"""

        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Update role's sort_order
        cur.execute(
            "UPDATE roles SET sort_order = ? WHERE id = ?",
            (key, str(id)),
        )

        # Commit and close connection
        con.commit()
        con.close()

    def update_role(self, role: Role) -> None:
        """This function can be used to update/modify the name, and/or description atributes of an existing role from the LifeVector database"""

        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Update role
        cur.execute(
            "UPDATE roles SET name = ?, description = ? WHERE id = ?",
            (role.name, role.description, str(role.id)),
        )

        # Commit and close connection
        con.commit()
        con.close()
