def connecttosnowflake:
    import snowflake.connector
    ctx = snowflake.connector.connect(
        user='user',
        password='password',
        account='account',
        warehouse='warehouse',
        database='database',
        schema='schema',
        role='role'
    )
    return ctx

