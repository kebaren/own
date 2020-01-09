datalist = {
    "rootMenu" :["File","Edit","View","Selection","Find","Packages","Help"],
    "File":[
        "New Window",
        "New File",
        "Open File",
        "Open Folder...",
        "Reopen Project",
        "Reopen Last Item",
        "Save",
        "Save As...",
        "Save All",
        "Close Tab",
        "Close Pane",
        "Close WIndow",
        "Quit",
        "Close All Tab"

    ],
    "Edit":[
        "Undo"
    ],
    "View":[
        "Toggle Full Screen"
    ],
    "Selection":[
        "Add Selection Above"
    ],
    "Find":[
        "Find in Buffer"
    ],
    "Packages":[
        "Packages And Themes"
    ],
    "Help":[
        "About Own"
    ]
}

menu_methods = {
    "File":["fileMethods.new_windwo","fileMethods.new_file","fileMethods.open_file","fileMethods.open_folder","fileMethods.reopen_project","fileMethods.reopen_last_item","fileMethods.save","fileMethods.save_as","fileMethods.save_all","fileMethods.close_tab","fileMethods.close_tab","fileMethods.close_pane","fileMethods.close_window","fileMethods.quit","fileMethods.close_all_tab"],
    "Edit":["editMethods.undo"],
    "View":["viewMethods.toggle_full_screen"],
    "Selection":["selectionMethods.add_selection_above"],
    "Find":["findMethods.find_in_buffer"],
    "Packages":["packageMethods.pacakge_and_themes"],
    "Help":["helpMethods.about_own"]
}
file_key_shot = {
    "new_windwo":"Ctrl+Shift+N"
}
