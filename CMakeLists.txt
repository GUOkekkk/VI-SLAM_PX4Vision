#include(${CMAKE_CURRENT_SOURCE_DIR}/../CMakeLists.txt)

#if(${ROS_VERSION} STREQUAL "2")

cmake_minimum_required(VERSION 3.5)
project(tf2_broadcaster)

## Compile as C++11, supported in ROS Kinetic and newer
#set(CMAKE_CXX_STANDARD 11)
#add_compile_options(-std=c++11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(ament_cmake REQUIRED)
find_package(ament_index_cpp REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)

###########
## Build ##
###########

include_directories(
                    include
                    ${rclcpp_INCLUDE_DIRS}
                    ${rmw_implementation_INCLUDE_DIRS}
                    ${std_msgs_INCLUDE_DIRS}
                    ${image_transport_INCLUDE_DIRS}
                    ${geometry_msgs_INCLUDE_DIRS}
                    ${tf2_INCLUDE_DIRS}
                    ${tf2_ros_INCLUDE_DIRS}
                    ${tf2_INCLUDE_DIRS}
                    ${tf2_geometry_msgs_INCLUDE_DIRS}
                    ${nav_msgs_INCLUDE_DIRS}
                    )


# build as executable
add_executable(tf2_broadcaster src/tf2_broadcaster_node.cpp)
target_link_libraries(tf2_broadcaster ${LINK_LIBRARIES})
 ament_target_dependencies(tf2_broadcaster
  rclcpp
  std_msgs
  tf2
  tf2_ros
  tf2_geometry_msgs
  nav_msgs
)

#############
## Install ##
#############


install(
  TARGETS tf2_broadcaster
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)


ament_package()

#endif()
