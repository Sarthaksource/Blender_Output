import bpy

def get_current_index(collection):
    return collection.get("current_index", 0)

def set_current_index(collection, current_index):
    collection["current_index"] = current_index

def disable_next_object_in_sequence(collection_name, head_name, bottom_name, top_name):    
    collection = bpy.data.collections.get(collection_name)
    objects_in_collection = collection.objects

    current_index = get_current_index(collection)
    
    if(current_index-1 >= 0):
        if(objects_in_collection[current_index-1]).hide_render == False :
            (objects_in_collection[current_index-1]).hide_render = True

    next_index = current_index % len(objects_in_collection)

    next_object = objects_in_collection[next_index]
    next_object.hide_render = False

    set_current_index(collection, next_index + 1)

    if(collection_name == "Head"):
        head_name[0] = next_object.name
    if(collection_name == "Bottom"):
        bottom_name[0] = next_object.name
    if(collection_name == "Top"):
        top_name[0] = next_object.name
    
    render(next_object, head_name[0], bottom_name[0], top_name[0])

def render(current_object, head_name, bottom_name, top_name):
    output_path = "G:/Animation/Test/"
    
    #start_frame = 1
    #end_frame = 5
    
    current_frame = bpy.context.scene.frame_current
    
    object_name = current_object.name

    file_path = bpy.path.abspath(f"{output_path}{head_name}_{top_name}_{bottom_name}")
    
    #file_path = bpy.path.abspath(f"{output_path}{current_frame}")

    bpy.context.scene.render.filepath = file_path
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    
    #bpy.context.scene.frame_start = start_frame
    #bpy.context.scene.frame_end = end_frame
        
    #bpy.ops.render.render(animation=True)

    bpy.ops.render.render(write_still=True)
        
#collection_name_to_target = "Val"

#print("AYO: ",Caller.a)

head_name = [""]
bottom_name = [""]
top_name = [""]
i=0

while(i<5):
    j=0
    disable_next_object_in_sequence("Head",head_name, bottom_name, top_name)
    while(j<5):
        k=0
        disable_next_object_in_sequence("Top",head_name, bottom_name, top_name)
        while(k<5):
            disable_next_object_in_sequence("Bottom",head_name, bottom_name, top_name)
            k += 1
        j += 1
    i += 1   

#disable_next_object_in_sequence(collection_name_to_target)