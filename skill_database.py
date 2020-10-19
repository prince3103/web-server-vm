import sqlite3

class SkillDatabase:
    def __init__(self):
        pass

    def getData(self, job_role, skill_type):
        '''
        conn : sqlite connection
        cursor : cursor object
        skill_type : checks if skill is hard or soft skill
        data : contains the data fetch from database
        '''
        try:
            #Connecting to sqlite
            conn = sqlite3.connect('career_map.db')

            #Creating a cursor object using the cursor() method
            cursor = conn.cursor()
            
            #Query to select data with following condition
            if skill_type=='both skill':
                cursor.execute("SELECT * FROM SKILLS WHERE JOB_ROLE IS '%s' COLLATE NOCASE ORDER BY FREQUENCY DESC;" %job_role)
            elif skill_type=='soft skill':
                cursor.execute("SELECT * FROM SKILLS WHERE JOB_ROLE IS '%s' COLLATE NOCASE AND SKILL_TYPE IS 'SOFT' ORDER BY FREQUENCY DESC;" %job_role)
            else:
                cursor.execute("SELECT * FROM SKILLS WHERE JOB_ROLE IS '%s' COLLATE NOCASE AND SKILL_TYPE IS 'HARD' ORDER BY FREQUENCY DESC;" %job_role)
            #statement to fetch data
            data = cursor.fetchall()

            # Commit your changes in the database
            conn.commit()

            #Closing the connection
            conn.close()

            return data
        except Exception as e:
            print("Error:",e)
            return []