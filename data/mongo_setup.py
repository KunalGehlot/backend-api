import mongoengine


def global_init():
    """Initialize the database"""
    mongoengine.register_connection(alias="default", name="family")
