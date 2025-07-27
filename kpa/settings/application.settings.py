"""Settings specifically related to application"""

# Would be used to validate data
REGEX_PATTERNS = {
    "axle_box_housing_bore_dia": r"^(\d+)\s\(([+-]?\d+\.?(?:\d+)?)\/([+-]?\d+\.?(?:\d+)?)\)$",  # 280 (+030/+0.052)
    "bearing_seat_diameter": r"^([+-]?\d+\.?(?:\d+)?) (?i:to) ([+-]?\d+\.?(?:\d+)?)",  # 130.043 TO 130.068
    "condemning_dia": r"^(\d+) \((\d+-\d+)\)",  # 825 (800-900)
    "intermediate_wwp": r"^([+-]?\d+\.?(?:\d+)?) (?i:to) ([+-]?\d+\.?(?:\d+)?)",  # 20 TO 80
    "last_shop_issue_size": r"^(\d+) \((\d+-\d+)\)",
    "roller_bearing_bore_dia": r"^(\d+)\s\(([+-]?\d+\.?(?:\d+)?)\/([+-]?\d+\.?(?:\d+)?)\)$",
    "roller_bearing_outer_dia": r"^(\d+)\s\(([+-]?\d+\.?(?:\d+)?)\/([+-]?\d+\.?(?:\d+)?)\)$",
    "roller_bearing_width": r"^(\d+)\s\(([+-]?\d+\.?(?:\d+)?)\/([+-]?\d+\.?(?:\d+)?)\)$",
    "tread_diameter_new": r"^(\d+) \((\d+-\d+)\)",
    "variation_same_axle": None,
    "variation_same_bogie": None,
    "variation_same_coach": None,
    "wheel_disc_width": r"^(\d+)\s\(([+-]?\d+\.?(?:\d+)?)\/([+-]?\d+\.?(?:\d+)?)\)$",
    "wheel_gauge": r"^(\d+)\s\(([+-]?\d+\.?(?:\d+)?)\,([+-]?\d+\.?(?:\d+)?)\)$",  # 1600 (+2,-1)
    "wheel_profile": None,
}
