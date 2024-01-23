import os

def get_project_path():
    """
    Get Project Directory
    :return:
    """
    project_name = "api_test_framework"
    file_path = os.path.dirname(__file__)
    return file_path[:file_path.find(project_name)+len(project_name)]

def sep(path, add_sep_before=False, add_sep_after=False):
    """
    Separator
    :param path: Directory List, Type is Array
    :param add_sep_before: If we need to add one separator before the directory
    :param add_sep_after: If we need to add one separator after the directory
    :return:
    """
    all_path=os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path