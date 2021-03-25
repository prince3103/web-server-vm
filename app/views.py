from flask import Blueprint
from flask_restplus import Api, Resource
import requests

from app import app

blueprint = Blueprint('api', __name__, url_prefix='/api/v1/career_map')
api = Api(blueprint, doc='/documentation', version='1.0.0', title='Career Map',
          description='API to predict skill map based on the job role provided'
          )


app.register_blueprint(blueprint)


ns = api.namespace('skills', description='Operations on Soft and Hard Skills')


@ns.route('/<string:job_role>')
@ns.doc(params={'job_role': {'description': 'Input Job Role for which you require skills'}},
        responses={200: 'Successful Operation', 404: 'Error: Resource Not Found'})
class Skill(Resource):
    @classmethod
    def get(cls, job_role):
        '''
        This function is called when a get request is made by client app  on skills endpoint.
        It calls get_data function from SkillDatabase module to extracts job skill, frequency
        and variants breakdown for both hard and soft skill
        from database.

        Parameters
        ----------
        job_role : Job Role input by user.

        Returns
        -------
        Dictionary
        '''
        job_role = job_role.strip()
        job_role = job_role.replace(" ", "_")

        # sending get request and saving the response as response object
        r = requests.get(url = "http://10.128.0.6:8080/data?job_role={job_role}&skill_type=both skill".format(job_role=job_role))

        # extracting data in json format
        job_result = r.json()

        return job_result


ns = api.namespace('soft_skills', description='Operations on Soft Skills')


@ns.route('/<string:job_role>')
@ns.doc(params={'job_role': {'description': 'Input Job Role for which you require soft skills'}},
        responses={200: 'Successful Operation', 404: 'Error: Resource Not Found'})
class SoftSkill(Resource):
    @classmethod
    def get(cls, job_role):
        '''
        This function is called when a get request is made by client app  on soft_skills endpoint.
        It calls get_data function from SkillDatabase module to extracts job skill, frequency
        and variants breakdown for soft skill from database.

        Parameters
        ----------
        job_role : Job Role input by user

        Returns
        -------
        Dictionary
        '''
        job_role = job_role.strip()
        job_role = job_role.replace(" ", "_")
        r = requests.get(url = "http://10.128.0.6:8080/data?job_role={job_role}&skill_type=soft skill".format(job_role=job_role))

        # extracting data in json format
        job_result = r.json()

        return job_result


ns = api.namespace('hard_skills', description='Operations on Hard Skills')


@ns.route('/<string:job_role>')
@ns.doc(params={'job_role': {'description': 'Input Job Role for which you require hard skills'}},
        responses={200: 'Successful Operation', 404: 'Error: Resource Not Found'})
class HardSkill(Resource):
    @classmethod
    def get(cls, job_role):
        '''
        This function is called when a get request is made by client app on hard_skills endpoint.
        It calls get_data function from SkillDatabase module to extracts job skill, frequency
        and variants breakdown for hard skill from database.

        Parameters
        ----------
        job_role : Job Role input by user

        Returns
        -------
        Dictionary
        '''
        job_role = job_role.strip()
        job_role = job_role.replace(" ", "_")
        r = requests.get(url = "http://10.128.0.6:8080/data?job_role={job_role}&skill_type=hard skill".format(job_role=job_role))

        # extracting data in json format
        job_result = r.json()

        return job_result
