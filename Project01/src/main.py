from app import InventoryList


def main():
    """Execute when it's the main execution module."""
    inv = InventoryList()
    inv.start_application()


# Call main() if this is the main execution module
if __name__ == '__main__':
    main()
