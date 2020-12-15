from dependency_injector import containers, providers
from src.services.import_contacts import ImportContacts
from src.services.csv_reader import CsvReader


class ImportContactsContainer(containers.DeclarativeContainer):

    # config = providers.Configuration()
    csvReader = CsvReader()

    importContactsService = providers.Factory(
        ImportContacts,
        read_file_service=csvReader,
    )