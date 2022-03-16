from os.path import join
from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder='templates', **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param template_name: имя шаблона
    :param folder: папка с шаблонами
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    # file_path = join(folder, template_name)
    # # Открываем шаблон по имени
    # with open(file_path, encoding='utf-8') as f:
    #     # Читаем
    #     template = Template(f.read())
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    # рендерим шаблон с параметрами
    return template.render(**kwargs)

