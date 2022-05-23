def my_var():

	dic_ = {
		"qd_int": 42,
		"qd_str": "42",
		"qd_lit": "quarante-deux",
		"qd_float": 42.0,
		"qd_bool": True,
		"qd_list": [42,],
		"qd_dict": {"42": 42},
		"qd_tuple": (42,),
		"qd_set": set()
	}

	for x in dic_:
		print(f"{dic_[x]} has a type {type(dic_[x])}")	

my_var()
