import mysql.connector
from mysql.connector import Error

class SkillDatabase:
    def __init__(self):
        pass

    @classmethod
    def get_data(cls, job_role, skill_type):
        '''
        This function establishes connection with database and extracts job skill,
        frequency and variants breakdown for a given job role and skill type

        Parameters
        ----------
        job_role : Job Role provided by user
        skill_type : Contains skill type(soft skill, hard skill, both skill)

        Returns
        -------
        List
        '''
        try:
            connection_config_dict = {
                'user': 'root',
                'password': '',
                'host': '10.128.0.6',
                'port': '3306',
                'database': 'career_map',
                'raise_on_warnings': True,
                'use_pure': False,
                'autocommit': True,
                'pool_size': 5
            }
            connection = mysql.connector.connect(**connection_config_dict)

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                # Creating a cursor object using the cursor() method
                cursor = connection.cursor()

                # Query to select data with following condition
                if skill_type == 'both skill':
                    cursor.execute(
                        "SELECT * FROM SKILLS;")
                elif skill_type == 'soft skill':
                    cursor.execute(
                        "SELECT * FROM SKILLS WHERE JOB_ROLE = '%s' COLLATE"
                        " NOCASE AND SKILL_TYPE IS 'Soft' AND SKILL_NAME!='none' ORDER"
                        " BY FREQUENCY DESC;" % job_role)
                else:
                    cursor.execute(
                        "SELECT * FROM SKILLS WHERE JOB_ROLE = '%s' COLLATE"
                        " NOCASE AND SKILL_TYPE IS 'Hard' AND SKILL_NAME!='none' ORDER"
                        " BY FREQUENCY DESC;" % job_role)
                # statement to fetch data""
                data = cursor.fetchall()

                # Commit your changes in the database
                connection.commit()
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
                return data

        except Error as e:
            print("Error while connecting to MySQL", e)
