#include <geometry_msgs/msg/transform_stamped.hpp>
#include <nav_msgs/msg/odometry.hpp>

#include <rclcpp/rclcpp.hpp>
#include <tf2/LinearMath/Quaternion.h>
#include <tf2_ros/transform_broadcaster.h>
#include <turtlesim/msg/pose.hpp>

#include <memory>
#include <string>

using std::placeholders::_1;

class FramePublisher : public rclcpp::Node
{
public:
  FramePublisher()
  : Node("tf2_broadcaster_node")
  {
    // Declare and acquire `topic_name_` parameter
    this->declare_parameter<std::string>("topic_name_", "/Drone9/EKF/odom");
    this->get_parameter("topic_name_", topic_name_);

    // Initialize the transform broadcaster
    tf_broadcaster_ =
      std::make_unique<tf2_ros::TransformBroadcaster>(*this);

    subscription_ = this->create_subscription<nav_msgs::msg::Odometry>(
      topic_name_,rclcpp::SensorDataQoS(),
      std::bind(&FramePublisher::handle_drone_pose, this, _1));
  }

private:
  void handle_drone_pose(const nav_msgs::msg::Odometry & msg)
  {
    rclcpp::Time now = this->get_clock()->now();
    geometry_msgs::msg::TransformStamped t;

    // Read message content and assign it to
    // corresponding tf variables
    t.header.stamp = now;
    t.header.frame_id = "odom";
    t.child_frame_id = "base_link";

    t.transform.translation.x = msg.pose.pose.position.x;
    t.transform.translation.y = msg.pose.pose.position.y;
    t.transform.translation.z = msg.pose.pose.position.z;

    t.transform.rotation.x = msg.pose.pose.orientation.x;
    t.transform.rotation.y = msg.pose.pose.orientation.y;
    t.transform.rotation.z = msg.pose.pose.orientation.z;
    t.transform.rotation.w = msg.pose.pose.orientation.w;

    // Send the transformation
    tf_broadcaster_->sendTransform(t);
  }
  rclcpp::Subscription<nav_msgs::msg::Odometry>::SharedPtr subscription_;
  std::unique_ptr<tf2_ros::TransformBroadcaster> tf_broadcaster_;
  std::string topic_name_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<FramePublisher>());
  rclcpp::shutdown();
  return 0;
}

