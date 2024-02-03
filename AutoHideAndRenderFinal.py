import bpy
import os

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
    output_path = "Path"

    # Use this for complete output
    # start_frame = 1
    # end_frame = 32
    
    current_frame = bpy.context.scene.frame_current
    
    object_name = current_object.name

    file_path = bpy.path.abspath(f"{output_path}{head_name}_{top_name}_{bottom_name}")
    
    # file_path = bpy.path.abspath(f"{output_path}{head_name}_{top_name}_{bottom_name}.mp4")    #Use it for mp4 output
    
    if os.path.exists(file_path):
        print(f"File {file_path} already exists. Skipping rendering.")
        return
    
    bpy.context.scene.render.filepath = file_path
    bpy.context.scene.render.image_settings.file_format = 'PNG'

    # Use these for mp4 output
    
    # bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    # bpy.context.scene.render.ffmpeg.format = 'MPEG4'
    # bpy.context.scene.render.ffmpeg.codec = 'H264'
    # bpy.context.scene.render.ffmpeg.constant_rate_factor = 'HIGH'
    
    # bpy.context.scene.frame_start = start_frame
    # bpy.context.scene.frame_end = end_frame  
    
    # bpy.ops.render.render(animation=True)

    # Use it for one frame output
    bpy.ops.render.render(write_still=True)

head_name = [""]
bottom_name = [""]
top_name = [""]
first_it=0

first_col_len = 5
second_col_len = 5
third_col_len = 5

while(first_it<first_col_len):
    second_it=0
    disable_next_object_in_sequence("Head",head_name, bottom_name, top_name)
    while(second_it<second_col_len):
        third_it=0
        disable_next_object_in_sequence("Top",head_name, bottom_name, top_name)
        while(third_it<third_col_len):
            disable_next_object_in_sequence("Bottom",head_name, bottom_name, top_name)
            third_it += 1
        second_it += 1
    first_it += 1   
