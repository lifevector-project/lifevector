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

    # Get all roles
    def get_all_roles(self) -> list[Role] | None:
        """This function returns a list of all the roles in the LifeVector database"""

        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Retrive data for all roles
        rows = cur.execute("SELECT * FROM roles ORDER BY sort_order ASC").fetchall()

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

    def remove_all_roles(self) -> None:
        """This function deletes all the roles from the LifeVector"""

        # Initiate a connection
        con = self.db_manager.connect()
        cur = con.cursor()

        # Remove all roles
        cur.execute("DELETE FROM roles")

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

    def set_sort_order(self, role_id, key):
        ...
    
    def get_active_roles(self):
        ...
    
    def get_last_sort_order(self):
        ...

    def get_first_sort_order(self):
        ...