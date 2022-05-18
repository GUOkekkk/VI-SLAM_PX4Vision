#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "nav_msgs/msg/odometry.hpp"
using std::placeholders::_1;

class Republisher : public rclcpp::Node
{
  public:
    Republisher()
    : Node("republisher")
    {
    this->declare_parameter<std::string>("topic_name_", "/Drone9/EKF/odom");
    this->get_parameter("topic_name_", topic_name_);

    subscription_ = this->create_subscription<nav_msgs::msg::Odometry>(topic_name_,rclcpp::SensorDataQoS(), 
    std::bind(&Republisher::republish_drone_pose, this, _1));
    
    publisher_ = this->create_publisher<nav_msgs::msg::Odometry>("/odom", 1);
    }

  private:  
    void republish_drone_pose(const nav_msgs::msg::Odometry & msg)
    {
    	nav_msgs::msg::Odometry republished;
	republished = msg;
	republished.header.frame_id = "odom";
	republished.child_frame_id = "base_link";
	// Republish the odometry, now with frame_id s
	publisher_->publish(republished);	
    }
    rclcpp::Subscription<nav_msgs::msg::Odometry>::SharedPtr subscription_;
    std::string topic_name_;
    rclcpp::Publisher<nav_msgs::msg::Odometry>::SharedPtr publisher_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Republisher>());
  rclcpp::shutdown();
  return 0;
}
