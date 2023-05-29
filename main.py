import user_function as uf
import API_classes as api
import vacancies_function as vf

if __name__ == "__main__":

    user_platform = uf.get_platform_from_user()
    if user_platform == 'HeadHunter.ru':
        user_region = uf.get_region_from_user()
        user_region_id = user_region['id']
        user_region_name = user_region['name']
        user_text = uf.get_text_from_user()
        user_salary = uf.get_salary_from_user()
        uf.show_summary_from_user(user_platform, user_region_name,
                                  user_text, user_salary)

        hh_api_data = api.HhVacancyAPI()
        hh_api_data.get_vacancies(user_text, user_region_id,
                                  user_salary)
        uf.show_vacancies_hh()
        vf.collect_hh_vacancies()
    else:
        user_text = uf.get_text_from_user()
        user_town = uf.get_town_from_user()
        user_salary = uf.get_salary_from_user()
        uf.show_summary_from_user(user_platform, user_town,
                                  user_text, user_salary)

        superjob_api_data = api.SuperJobVacancyAPI()
        superjob_api_data.get_vacancies(user_text, user_town,
                                        user_salary)
        uf.show_vacancies_sj()
        vf.collect_sj_vacancies()

