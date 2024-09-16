import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import ExecuteProcess
from launch.actions import OpaqueFunction
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Definisci il percorso al tuo file SDF (mondo)
    world_file_name = 'leonardo_race_field.sdf'
    world_path = os.path.join(
        get_package_share_directory('leonardo_field_description'),
        'worlds',
        world_file_name
    )

    # Comando per lanciare Gazebo Garden con il mondo specificato
    gazebo_cmd = ExecuteProcess(
        cmd=['gz', 'sim', '-r', world_path], 
        output='screen'
    )

    return LaunchDescription([
        # Lancia Gazebo Garden con il mondo definito
        gazebo_cmd,
    ])
