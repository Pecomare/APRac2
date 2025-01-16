class Addresses:
    """ Addresses for important memory locations on the Ratchet and Clank 2 'SCUS-97268' ISO """
    # Functions in Core memory
    MAIN_LOOP_FUNC: int = 0x0028B518

    # Functions that appear and multiple planets
    GO_STARTING_PLANET_FUNCS: list[int] = [0x0044FBD8, 0x94A54B44]
    TITLE_SCREEN_MAIN_FUNC: int = 0x003C8568
    QUIT_TITLE_MAIN_FUNC: int = 0x949CE704
    PLANET_MAIN_FUNCS: list[int] = [
        0x9D2B762C, 0x9EB45A94, 0xA19640F8, 0xA5E015C0, 0xA8F28FBC, 0xACAC3ECC, 0xAE3F2CCC, 0xB0734480, 0xB2F97F7C,
        0xB6BA87CC, 0xB97B4384, 0xBAF7E948, 0xBF9791A8, 0xC32C65B4, 0xC6282DEC, 0xC8EF2C90, 0xCA5666D0, 0xCD92E3B4,
        0xD0075528, 0xD23C40C0, 0xD673F210, 0xDAE92C44, 0xDCC59C30, 0xDE819B84, 0xDF9D1F00, 0xE0632FD0, 0xE14CF47C
    ]
    PLAT_BOLT_UPDATE_FUNCS: list[int] = [
        0x9EC36EAC, 0xA1A67F78, 0xA5EFE1D0, 0xA902524C, 0xAE4F5ED4, 0xB0827870, 0xB309287C, 0xB6CA1D2C, 0xBB079120,
        0xBFA76DA8, 0xC33C4DCC, 0xC63846F4, 0xCA65D330, 0xCDA2ED84, 0xD0173F08, 0xD24BC5A0, 0xD6847A80, 0xDCD5E4C0,
        0xDE91E30C, 0xE15CA79C
    ]
    PLAT_BOLT_COUNT_FUNCS: list[int] = [
        0x0040A538, 0x94A0F8FC, 0x9D33A494, 0x9EBBC1EC, 0xA19E8D40, 0xA5E7E8D0, 0xA8FA6AEC, 0xACB44D44, 0xAE47689C,
        0xB07AD3E0, 0xB30171BC, 0xB6C244E4, 0xB9834A5C, 0xBAFFA930, 0xBF9F9DF0, 0xC334730C, 0xC630630C, 0xC8F74C08,
        0xCA5E0280, 0xCD9B1FCC, 0xD00F4CD8, 0xD2440940, 0xD67C4898, 0xDAF135F4, 0xDCCDD5C8, 0xDE89D534, 0xDFA51770,
        0xE06B3670, 0xE155111C
    ]
    NANOTECH_BOOST_UPDATE_FUNCS: list[int] = [
        0xA5F7BEF8, 0xACC32024, 0xAE573D74, 0xB310FA9C, 0xB6D22774, 0xBB135CF8, 0xBFAF5FD8, 0xC343C2F4, 0xCA6DF7E0
    ]
    NANOTECH_COUNT_FUNCS: list[int] = [
        0x9D2E995C, 0x9EB6B194, 0xA19965F8, 0xA5E2DC48, 0xA8F541DC, 0xACAF61B4, 0xAE42517C, 0xB075C160, 0xB2FC3794,
        0xB6BD3224, 0xB97E666C, 0xBAFA97F0, 0xBF9A9108, 0xC32F83EC, 0xC62B529C, 0xC8F24F78, 0xCA5903A0, 0xCD96023C,
        0xD00A4178, 0xD23F03F0, 0xD67728B8, 0xDAEC4FC4, 0xDCC8E3D0, 0xDE84E304, 0xDFA041E8, 0xE06652B8, 0xE15018E4
    ]
    SETUP_RATCHET_FUNCS: list[int] = [
        0x9D2B83CC, 0x9EB46834, 0xA1964E98, 0xA5E02360, 0xA8F29D5C, 0xACAC4C6C, 0xAE3F3A6C, 0xB0735220, 0xB2F98D1C,
        0xB6BA956C, 0xB97B5124, 0xBAF7F6E8, 0xBF979F48, 0xC32C7354, 0xC6283B8C, 0xC8EF3A30, 0xCA567470, 0xCD92F154,
        0xD00762C8, 0xD23C4E60, 0xD673FFB0, 0xDAE939E4, 0xDCC5A9D0, 0xDE81A924, 0xDF9D2CA0, 0xE0633D70, 0xE14D021C
    ]
    UNLOCK_PLANET_FUNCS: list[int] = [
        0x00406F38, 0x94A0C2FC, 0x9D334F5C, 0x9EBB6F14, 0xA19E2AA0, 0xA5E79B18, 0xA8FA100C, 0xACB40974, 0xAE471F14,
        0xB07A79D8, 0xB3011DBC, 0xB6C1ECC4, 0xB983118C, 0xBAFF5800, 0xBF9F4AE0, 0xC3342E54, 0xC63009E4, 0xC8F6FF60,
        0xCA5DBD88, 0xCD9AC764, 0xD00EFDE0, 0xD243BBC8, 0xD67BF198, 0xDAF0F9FC, 0xDCCD88A8, 0xDE898814, 0xDFA4E018,
        0xE06AF418, 0xE154C8E4
    ]
    SETUP_PLANET_FUNCS: list[int] = [
        0x003E9ED8, 0x949EF9DC, 0x9D30FBB4, 0x9EB91584, 0xA19BD4B0, 0xA5E548D0, 0xA8F7A98C, 0xACB1C114, 0xAE44B12C,
        0xB0782A00, 0xB2FE9B9C, 0xB6BF9754, 0xB980C5E4, 0xBAFD0328, 0xBF9CF408, 0xC331E20C, 0xC62DB77C, 0xC8F4AED8,
        0xCA5B6BA8, 0xCD9862AC, 0xD00CA3B8, 0xD2416488, 0xD67990E8, 0xDAEEB12C, 0xDCCB3CC8, 0xDE873C3C, 0xDFA29AC8,
        0xE068AE68, 0xE1527664
    ]
    PLANET_UNLOCK_MESSAGE_FUNCS: list[int] = [
        0x00408828, 0x94A0DBEC, 0x9D337A9C, 0x9EBB8E6C, 0xA19E5648, 0xA8FA3EC4, 0xACB42EDC, 0xAE473CBC, 0xB30145E4,
        0xB6C21764, 0xB9832BF4, 0xBAFF7C68, 0xBF9F6888, 0xC3344BFC, 0xC630356C, 0xC8F72800, 0xCD9AF39C, 0xD00F2778,
        0xD243E668, 0xD67C1138, 0xDCCDB1C0, 0xDE89B12C, 0xE154E904
    ]
    RACE_CONTROLLER_FUNCS: list[int] = [0xACC33874, 0xB9922C6C, 0xC906D080]
    IS_BUYABLE_FUNCS: list[int] = [
        0x003E1E48, 0x949E794C, 0x9D307764, 0x9EB88B34, 0xA19B4E38, 0xA5E4BE80, 0xA8F7253C, 0xACB13CAC, 0xAE442CDC,
        0xB077A1D8, 0xB2FE149C, 0xB6BF1304, 0xB980417C, 0xBAFC7CB0, 0xBF9C6FB8, 0xC3315DBC, 0xC62D332C, 0xC8F42A70,
        0xCA5AE380, 0xCD97DE5C, 0xD00C1F68, 0xD240DFB0, 0xD67908C0, 0xDAEE2CDC, 0xDCCAB878, 0xDE86B7EC, 0xDFA21678,
        0xE0682A00, 0xE151F214
    ]
    AVAILABLE_ITEM_FUNCS: list[int] = [
        0x003EA0F8, 0x949EFBFC, 0x9D30FDD4, 0x9EB917A4, 0xA19BD6D0, 0xA5E54AF0, 0xA8F7ABAC, 0xACB1C334, 0xAE44B34C,
        0xB0782C20, 0xB2FE9DBC, 0xB6BF9974, 0xB980C804, 0xBAFD0548, 0xBF9CF628, 0xC331E42C, 0xC62DB99C, 0xC8F4B0F8,
        0xCA5B6DC8, 0xCD9864CC, 0xD00CA5D8, 0xD24166A8, 0xD6799308, 0xDAEEB34C, 0xDCCB3EE8, 0xDE873E5C, 0xDFA29CE8,
        0xE068B088, 0xE1527884
    ]
    POPULATE_VENDOR_SLOT_FUNCS: list[int] = [
        0x0044FD88, 0x94A54CF4, 0x9D384C54, 0x9EC06EDC, 0xA1A35B30, 0xA5EC9938, 0xA8FF26DC, 0xACB8DE64, 0xAE4C20AC,
        0xB07F74E0, 0xB30611AC, 0xB6C6F7F4, 0xB987DAFC, 0xBB0474B8, 0xBFA46428, 0xC339251C, 0xC63533A4, 0xC8FC2F90,
        0xCA62A0A0, 0xCD9FDA64, 0xD0140D58, 0xD248BC18, 0xD680FA40, 0xDAF59A94, 0xDCD26B58, 0xDE8E6AC4, 0xDFA976B0,
        0xE06FC490, 0xE159BC4C
    ]
    VENDOR_REQUIREMENT_TABLES: list[int] = [
        0x00399B40, 0x9499FF0C, 0x9D27C93C, 0x9EB09B90, 0xA192861C, 0xA5DC497C, 0xA8EDF884, 0xACA86E60, 0xAE382BFC,
        0xB06F94A0, 0xB2F550E4, 0xB6B6CDA4, 0xB9777220, 0xBAF41FCC, 0xBF939A7C, 0xC328B5E4, 0xC6246AD4, 0xC8EB3BB4,
        0xCA52B9A4, 0xCD8F30A4, 0xD00260DC, 0xD2388C48, 0xD66FCD7C, 0xDAE57FA4, 0xDCC1D164, 0xDE7DAE44, 0xDF997A04,
        0xE05F6170, 0xE1493EB4
    ]

    # Oozla
    MEGACORP_SCIENTIST_FUNC: int = 0x9EC7295C
    DYNAMO_PICKUP_FUNC: int = 0x9EC6E8AC
    BOX_BREAKER_PICKUP_FUNC: int = 0x9ECB5F4C
    SWAMP_MONSTER_GATE_FUNC: int = 0x9ECA4E0C
    OOZLA_CONTROLLER_FUNC: int = 0x9EC889E4

    # Maktar
    MAKTAR_CONTROLLER_FUNC: int = 0xA1AC6FE8
    ARENA_CONTROLLER_FUNC: int = 0xA1AB6E80
    ELECTROLYZER_REWARD_TEXT: int = 0x975A7778
    PHOTO_BOOTH_FUNC: int = 0xA1ACCDF0
    JAMMING_ARRAY_LIMO_FUNC: int = 0xE15FDC64

    # Endako
    ENDAKO_CONTROLLER_FUNC: int = 0xA5F47C78
    APARTMENT_PICKUP_FUNC: int = 0xA5F48728
    POST_CLANK_BUTTON_FUNC: int = 0xA5F28C80
    FREE_RATCHET_FUNC: int = 0xA5F293B0

    # Barlow
    INVENTOR_FUNC: int = 0xA90926E4
    BIKER_ONE_FUNC: int = 0xA9080D8C
    BARLOW_SPAWN_CONTROLLER_FUNC: int = 0xA90B415C

    # Feltzin
    NOTAK_COORDS_TEXT: int = 0x975B43F4

    # Notak
    WORKER_BOTS_FUNC: int = 0xAE53FE5C
    SECRET_MESSAGE_FUNC: int = 0xAE4F0B8C

    # Siberius
    THIEF_FUNC: int = 0xB0887340

    # Tabora
    ANGELA_CUTSCENE_FUNC: int = 0xB30EFEEC
    TABORA_CONTROLLER_FUNC: int = 0xB30D890C
    GLIDER_PICKUP_FUNC: int = 0xB30F04AC

    # Dobbo
    TERMINAL_FUNC: int = 0xB6D0973C
    MATHEMATICIAN_FUNC: int = 0xB6D0B5AC

    # Joba
    BIKER_TWO_FUNC: int = 0xBB0BA050
    SHADY_MERCHANT_FUNC: int = 0xBB123400
    ARENA2_CONTROLLER_FUNC: int = 0xBB0FFCE0
    ARENA2_REWARD_FUNC: int = 0xBB1042F8
    ARENA2_EXIT_FUNC: int = 0xBB104108
    JOBA_CONTROLLER_FUNC: int = 0xBB134950

    # Todano
    STUART_ZURGO_FUNC: int = 0xBFA84CE0
    SHEEPINATOR_PICKUP_FUNC: int = 0xBFAD2898

    # Boldan
    BOLDAN_CUTSCENE_TRIGGER_FUNC: int = 0xC34347CC

    # Aranos Prison
    PLUMBER_FUNC: int = 0xC63FD794
    PRISON_CONTROLLER_FUNC: int = 0xC63FE09C

    # Smolg
    # HYPNOMATIC_PART1_FUNC: int = 0xCDAA8084

    # Damosel
    DAMOSEL_CONTROLLER_FUNC: int = 0xD01ACB40
    HYPNOMATIC_PART2_FUNC: int = 0xD01F3710
    HYPNOTIST_FUNC: int = 0xD01F41B8

