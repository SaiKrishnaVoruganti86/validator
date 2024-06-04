changed name from   pattern: '^[A-Za-z0-9_.-]*$' to   pattern: '^[A-Za-z0-9.,-_/]*$'
changed id from   pattern: '^((urn:sdx:topology:)[A-Za-z0-9_.:-]*$)' to   pattern: '^urn:sdx:topology:[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
version reamined same
model_version previously only type: string, now added as pattern: ^2\.0\.0$
timestamp changed from format: date-time to pattern: '^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])T([01]\d|2[0-3]):([0-5]\d):([0-5]\d)Z$'

changes on nodes:
added -status -state in required: of nodes.
changed name from pattern: '^[A-Za-z0-9_.-]*$' to pattern: '^[a-zA-Z0-9.,\-_\/]{1,30}$'
changed id from pattern: '^((urn:sdx:node:)[A-Za-z0-9_.\:/-]*$)'to '^urn:sdx:node:[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}:[a-zA-Z0-9.,\-_\/]{1,30}$'
added: status and in required,
    status:
        type: string
        enum: [up, down, error]
added: state in required,
    state:
        type: string
        enum: [enabled, disabled, maintenance]