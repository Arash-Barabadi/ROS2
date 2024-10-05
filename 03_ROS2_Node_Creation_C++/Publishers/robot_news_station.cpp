#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class RobotNewsStationNode : public rclcpp::Node
{
public:
    /// we create a publisher here 
    // the name of the node is : "robot_news_station"
    RobotNewsStationNode() : Node("robot_news_station"), robot_name_("R2D2")
    {
        // We initialize our publisher here
        // topic is "robot_news", and queue size is 10.  
        publisher_ = this->create_publisher<example_interfaces::msg::String>("robot_news", 10);

        // here we will initialize the timer 
        timer_ = this->create_wall_timer(std::chrono::milliseconds(500),
                                         std::bind(&RobotNewsStationNode::publishNews, this));

        // we have added a line to print something 
        RCLCPP_INFO(this->get_logger(), "Robot News Station has been started.");
    }

private:

    // to publish on this topic, we will create a function. 
    //We will call the following publishnews() function with a timer. We will define a time on line ///$$$///.
    void publishNews()
    {
        auto msg = example_interfaces::msg::String();
        msg.data = std::string("Hi, this is ") + robot_name_ + std::string(" from the Robot News Station");
        publisher_->publish(msg);
    }

    // Now we will customize the String "Hi, this is ...." as follows.
    std::string robot_name_;


    /// before we create a publisher, we have to decalre the publisher as follows. 
    // rclcpp::Publisher
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;

    //$$$// we are going to declare a timer here, to call the publishnews() function.  
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewsStationNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
