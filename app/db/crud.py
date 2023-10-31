import psycopg2 as psy
import csv



# host_="10.61.11.10"
# dbname_="devices"
# user_="conso"
# password_="kwakkwak"
# connection = psy.connect(host=host_, dbname=dbname_, user=user_, password=password_)



    
def create_table_devices_consumption():
    print("creating table")
    connection = psy.connect("postgres://mulder974:lKbZ12dmkqXi@ep-sweet-night-02972674.eu-central-1.aws.neon.tech/neondb")

    connection.set_session(autocommit=True)
    cursor = connection.cursor()

    cursor.execute(
        """
      CREATE TABLE IF NOT EXISTS devices_consumption (
    id SERIAL PRIMARY KEY,
    device_name VARCHAR,    
    cunsumption_1 FLOAT,
    consumption_2 FLOAT);
        """
    )

    print("table created")
    connection.close()


def insert_data_devices_consumption():
    with open('resultats.csv', mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row if it exists

        for row in csv_reader:
            print(row)
            device_name = row[1]
            consumption_1 = float(row[2])
            consumption_2 = float(row[3])
            print("inserting device : " + device_name + "Consumption : " + str(consumption_1) + "/" + str(
                consumption_2) + " in db")

            connection = psy.connect("postgres://mulder974:lKbZ12dmkqXi@ep-sweet-night-02972674.eu-central-1.aws.neon.tech/neondb")
            connection.set_session(autocommit=True)
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO devices_consumption (device_name, cunsumption_1, consumption_2) VALUES (%s, %s, %s)",
                (device_name, consumption_1, consumption_2))




def get_all_device_names():
    connection = psy.connect("postgres://mulder974:lKbZ12dmkqXi@ep-sweet-night-02972674.eu-central-1.aws.neon.tech/neondb")
    connection.set_session(autocommit=True)
    cursor = connection.cursor()

    cursor.execute("SELECT device_name FROM devices_consumption")
    device_names = cursor.fetchall()

    connection.close()

    # Convert list of tuples to a simple list
    device_names_list = [item[0] for item in device_names]

    return  device_names_list


def get_energy_consumption(device_name):
    connection = psy.connect("postgres://mulder974:lKbZ12dmkqXi@ep-sweet-night-02972674.eu-central-1.aws.neon.tech/neondb")
    connection.set_session(autocommit=True)
    cursor = connection.cursor()

    cursor.execute("SELECT cunsumption_1, consumption_2 FROM devices_consumption WHERE device_name = %s",
                   (device_name,))
    energy_data = cursor.fetchone()

    connection.close()

    return energy_data

create_table_devices_consumption()
insert_data_devices_consumption()