output_dictionary_part = dict()
sub_dict = dict()
output_list = list()


def dictionary_part_creation(input_dictionary_part):
    # создаем словарь-часть из ЭЛЕМЕНТА входного списка
    sub_dict["count"] = int(input_dictionary_part["count"] - input_dictionary_part["return_count"])
    sub_dict["id"] = int(input_dictionary_part["item_id"])
    output_dictionary_part["id"] = int(input_dictionary_part["order_id"])
    output_dictionary_part["items"] = sub_dict
    return output_dictionary_part


def result_creation(input_sorted_list):
    # разбиваем входной список УЖЕ ОТСОРТИРОВАННЫЙ ПО ИВЕНТАМ по элементам, где каждый элемент - словарь
    for i in range(0, len(input_sorted_list)):
        input_part = input_sorted_list[i]
        # проверим на пригодность каждый словарь
        if input_part["status"] == "CANCEL" or int(input_part["count"] - input_part["return_count"]) == 0 \
                or input_part["count"] == 0:
            pass
        else:
            adding = dictionary_part_creation(input_part)
            # добавляем словарь-часть в финальный список
            output_list.append(adding)
    return output_list


def event_sort(input_list):
    # создадим копию для работы с ней
    copy_list = input_list
    for k in range(0, len(input_list)):
        for m in range(k + 1, len(input_list)):
            # будем сравнивать k-ый и m-ый элементы-словари
            k_dict = input_list[k]
            m_dict = input_list[m]
            if k_dict["order_id"] == m_dict["order_id"] and k_dict["event_id"] > m_dict["event_id"]:
                copy_list.remove()