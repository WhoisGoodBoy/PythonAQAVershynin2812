



def test_check_phones_listing(phone):
    list_of_phones = phone.get_list_of_all_objects()
    assert list_of_phones.status_code == 200
    print(list_of_phones.json())

def test_check_single_phone(phone):
    single_phone = phone.get_single_phone(10)
    assert single_phone.status_code == 200
    print(single_phone.json())

def test_create_phone_with_default_value(phone):
    default_phone = phone.create_single_default_object()
    print(default_phone.json())
    assert default_phone.status_code == 200
    assert default_phone.json()['createdAt']

def test_update_single_phone_with_default_value(phone):
    default_updated_object = phone.update_single_default_object()
    assert default_updated_object.status_code == 200
    assert default_updated_object.json()['updatedAt']
    print(default_updated_object.json())

def test_patch_name(phone):
    default_patched_phone = phone.patch_single_default_object(phone.upadted_name)
    assert default_patched_phone.status_code == 200
    print(default_patched_phone.json())

def test_patch_data_correct(phone):
    default_patched_phone = phone.patch_single_default_object(phone.updated_data_correct_one)
    assert default_patched_phone.status_code == 200
    print(default_patched_phone.json())

def test_patch_data_incorrect(phone):
    default_patched_phone = phone.patch_single_default_object(phone.updated_data_incorrect_one)
    assert default_patched_phone.status_code == 200
    print(default_patched_phone.json())

def test_object_deletion(phone):
    deleted_object, deleted_object_id = phone.delete_default_object()
    assert deleted_object.json()['message'] == f"Object with id = {deleted_object_id} has been deleted."

def test_filter_dogs(dog_pack, dog):
    list_of_filtered_dogs = dog.filter_only_dogs(dog_pack)
    assert list_of_filtered_dogs.status_code == 200
    print(list_of_filtered_dogs.json())

