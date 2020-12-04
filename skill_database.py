"""
This module extracts skill name, frequency and variants breakdown for a
given job role and skill type
"""
import sqlite3


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
            # Connecting to sqlite
            conn = sqlite3.connect('career_map.db')

            # Creating a cursor object using the cursor() method
            cursor = conn.cursor()

            # Query to select data with following condition
            if skill_type == 'both skill':
                cursor.execute(
                    "SELECT * FROM SKILLS WHERE JOB_ROLE IS '%s' COLLATE"
                    " NOCASE AND SKILL_NAME!='none' ORDER BY FREQUENCY DESC;" % job_role)
            elif skill_type == 'soft skill':
                cursor.execute(
                    "SELECT * FROM SKILLS WHERE JOB_ROLE IS '%s' COLLATE"
                    " NOCASE AND SKILL_TYPE IS 'Soft' AND SKILL_NAME!='none' ORDER"
                    " BY FREQUENCY DESC;" % job_role)
            else:
                cursor.execute(
                    "SELECT * FROM SKILLS WHERE JOB_ROLE IS '%s' COLLATE"
                    " NOCASE AND SKILL_TYPE IS 'Hard' AND SKILL_NAME!='none' ORDER"
                    " BY FREQUENCY DESC;" % job_role)
            # statement to fetch data""
            data = cursor.fetchall()

            # Commit your changes in the database
            conn.commit()

            # Closing the connection
            conn.close()

            return data
        except Exception as e:
            print("Error:", e)
            return []
