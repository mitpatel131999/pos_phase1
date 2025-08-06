from werkzeug.security import generate_password_hash, check_password_hash

class User:
    """
    User model with basic password hashing and role-based permissions.
    This class mimics the essential behaviour of the original User model
    from the monolithic POS backend while keeping the code self-contained.
    """

    # Example permissions mapping for different roles
    role_permissions = {
        'owner': {
            'manage_users': True,
            'manage_products': True,
            'manage_transactions': True,
            'manage_orders': True,
            'view_reports': True,
        },
        'admin': {
            'manage_users': True,
            'manage_products': True,
            'manage_transactions': True,
            'manage_orders': True,
            'view_reports': True,
        },
        'cashier': {
            'manage_users': False,
            'manage_products': False,
            'manage_transactions': True,
            'manage_orders': True,
            'view_reports': False,
        },
    }

    @staticmethod
    def generate_hash(password: str) -> str:
        """Generate a hashed password."""
        return generate_password_hash(password)

    @staticmethod
    def verify_hash(password: str, hashed: str) -> bool:
        """Verify a password against a given hash."""
        return check_password_hash(hashed, password)

    @staticmethod
    def get_permissions_for_role(role: str):
        """Return the permissions dictionary for a given user role."""
        return User.role_permissions.get(role, {})
