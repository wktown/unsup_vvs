{
"BATCH_SIZE": 8,
"QUEUE_CAP": 2560,
"encode_depth": 32,
"up_projection_depth": 3,
"normal_depth": 1,
"depth_depth": 1,
"place_category_depth": 2,
"category_depth": 2,
"ins_decode_depth": 17,
"pbr_instance_depth": 1,
"coco_instance_depth": 1,
"scene_instance_depth": 1,
"network_list": ["encode", "up_projection", "normal", "depth", "ins_decode", "pbr_instance", "coco_instance", "category", "place_category", "scene_instance"],
"pbrnet_order": ["encode", "up_projection", "normal", "depth"],
"scenenet_order": ["encode", "up_projection", "normal", "depth"],
"imagenet_order": ["encode", "category"],
"place_order": ["encode", "place_category"],
"coco_order": ["encode", "ins_decode", "coco_instance"],
"nyuv2_order": ["encode", "up_projection", "depth"],
"encode": {
    "1": {"conv": {"filter_size": 7, "stride": 2, "num_filters": 64, "bn": 1, "padding": "VALID"}},
    "2": {"pool": {"filter_size": 3, "type": "max", "stride": 2}},
    "3": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 64, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 64, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}]},
    "4": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 64, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 64, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}]},
    "5": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 64, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 64, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}]},
    "6": {"ResBlock": [{"filter_size": 1, "stride": 2, "num_filters": 128, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 128, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 512, "bn": 1}]},
    "7": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 128, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 128, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 512, "bn": 1}]},
    "8": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 128, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 128, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 512, "bn": 1}]},
    "9": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 128, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 128, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 512, "bn": 1}]},
    "10": {"ResBlock": [{"filter_size": 1, "stride": 2, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "11": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "12": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "13": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "14": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "15": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "16": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "17": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "18": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "19": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "20": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "21": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "22": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "23": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "24": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "25": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "26": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "27": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "28": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "29": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "30": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "31": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]},
    "32": {"ResBlock": [{"filter_size": 1, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, {"filter_size": 1, "stride": 1, "num_filters": 1024, "bn": 1}]}
    },
"up_projection":{
    "input": "encode_32",
    "1": {"UpProj": {"filter_size": 3, "num_filters": 256, "bn": 1}},
    "2": {"UpProj": {"filter_size": 3, "num_filters": 128, "bn": 1}},
    "3": {"UpProj": {"filter_size": 3, "num_filters": 64, "bn": 1}}
    },
"normal":{
    "input": "up_projection_3",
    "as_output": 1,
    "1": {"conv": {"filter_size": 3, "stride": 2, "num_filters": 3, "output": 1, "upsample": 2}}
    },
"depth":{
    "input": "up_projection_3",
    "as_output": 1,
    "1": {"conv": {"filter_size": 3, "stride": 2, "num_filters": 1, "output": 1, "upsample": 2}}
    },
"ins_decode": {
    "input": "encode_18",
    "1": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 512, "bn": 1}},
    "2": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 512, "bn": 1}, "bypass": ["encode_17"]},
    "3": {"conv": {"filter_size": 3, "stride": 2, "num_filters": 512, "bn": 1, "upsample": 2}, "bypass": ["encode_16"]},
    "4": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, "bypass": ["encode_15"]},
    "5": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, "bypass": ["encode_14"]},
    "6": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, "bypass": ["encode_13"]},
    "7": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, "bypass": ["encode_12"]},
    "8": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 256, "bn": 1}, "bypass": ["encode_11"]},
    "9": {"conv": {"filter_size": 3, "stride": 2, "num_filters": 256, "bn": 1, "upsample": 2}, "bypass": ["encode_10"]},
    "10": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 128, "bn": 1}, "bypass": ["encode_9"]},
    "11": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 128, "bn": 1}, "bypass": ["encode_8"]},
    "12": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 128, "bn": 1}, "bypass": ["encode_7"]},
    "13": {"conv": {"filter_size": 3, "stride": 2, "num_filters": 128, "bn": 1, "upsample": 2}, "bypass": ["encode_6"]},
    "14": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 64, "bn": 1}, "bypass": ["encode_5"]},
    "15": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 64, "bn": 1}, "bypass": ["encode_4"]},
    "16": {"conv": {"filter_size": 3, "stride": 1, "num_filters": 64, "bn": 1}, "bypass": ["encode_3"]},
    "17": {"conv": {"filter_size": 3, "stride": 2, "num_filters": 64, "bn": 1, "upsample": 2}, "bypass": ["encode_2"]}
    },
"pbr_instance":{
    "input": "ins_decode_17",
    "as_output": 1,
    "1": {"conv": {"filter_size": 3, "stride": 2, "num_filters": 40, "output": 1, "upsample": 2}, "bypass": ["encode_1"]}
    },
"coco_instance":{
    "input": "ins_decode_17",
    "as_output": 1,
    "1": {"conv": {"filter_size": 3, "stride": 2, "num_filters": 92, "output": 1, "upsample": 2}, "bypass": ["encode_1"]}
    },
"scene_instance":{
    "input": "ins_decode_17",
    "as_output": 1,
    "1": {"conv": {"filter_size": 3, "stride": 2, "num_filters": 260, "output": 1, "upsample": 2}, "bypass": ["encode_1"]}
    },
"category":{
    "input": "encode_32",
    "as_output": 1,
    "1": {"pool": {"filter_size": 7, "type": "avg", "stride": 1, "padding": "VALID"}},
    "2": {"fc": {"num_features": 1000, "output": 1}}
    },
"place_category":{
    "input": "encode_18",
    "as_output": 1,
    "1": {"pool": {"filter_size": 7, "type": "avg", "stride": 1, "padding": "VALID"}},
    "2": {"fc": {"num_features": 365, "output": 1}}
    }
}
