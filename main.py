import user_function as uf
import API_classes as api

if __name__ == "__main__":

    user_platform = uf.get_platform_from_user()
    user_region = uf.get_region_from_user()
    user_region_id = user_region['id']
    user_region_name = user_region['name']
    user_text = uf.get_text_from_user()
    user_salary = uf.get_salary_from_user()
    uf.show_summary_from_user(user_platform, user_region_name,
                              user_text, user_salary)

    if user_platform == 'HeadHunter.ru':
        hh_api_data = api.HhVacancyAPI()
        hh_api_data.get_vacancies(user_text, user_region_id,
                                  user_salary)
        uf.show_vacancies()
    else:
        pass

    # vakansy = HhVacancyAPI()
    # vakansy_HH.get_vacancies('Pytnon', '1124', 50000)
    # vakansy_HH.get_russian_areas()
