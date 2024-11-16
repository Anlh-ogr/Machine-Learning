# Reinforcement Learning

## **Detail**

**Môi ttrường CartPole trong OpenAI Gym là một bài học tăng cường (Reinforcement Learning) cổ điển, phổ biến trong việc thử nghiệm các thuật toán RL.**

## Overview

**CartPole là bài toán điều khiển một cột/con lắc gắn trên một xe đẩy chuyển động dọc theo đường ray. Mục tiêu duy nhất là giữ cho cột đứng thẳng bằng cách tác dụng lực đẩy (force) lên xe đẩy theo hướng trái hoặc phải.**

## Problem structure

- **State: môi trường được biểu diễn bởi một không gian trạng thái 4 chiều:**
    - **Vị trí xe đẩy (x).**
    - **Vận tốc xe đẩy (x’).**
    - **Góc của cột so với phương thẳng đứng (θ).**
    - **Vận tốc góc của cột (θ’).**
- **Action: môi trường có hai hành động rời rạc:**
    - **0: Tác dụng lực sang trái.**
    - **1 : Tác dụng lực sang phải.**
- **Reward: tạo hàm thưởng:**
    - **+1 điểm được thưởng ở mỗi bước nếu cột vẫn đứng thẳng.**
- **Termination: điều kiện kết thúc:**
    - **Cột nghiên quá ±12° so với phương thẳng đứng.**
    - **Xe đẩy đi ra khỏi biên của đường ray (|x| > 2.4).**
    - **Tập trung tối đa vào việc duy trì trạng thái này càng lâu càng tốt.**
- **Target:**
    - **Tối đa hóa tổng điểm nhận được trong một tập (episode).**

## **Physical characteristics of the system**

- **Khớp quay: Cột được gắn bằng một khớp quay không có cơ cấu truyền động.**
- **Xe đẩy di chuyển trên đường ray không ma sát: Chuyển động của xe đẩy không bị ảnh hưởng bởi ma sát với mặt đường.**
- **Mô hình động lực học: Mô hình dựa trên phương trình chuyển động của con lắc ngược. Các dữ liệu vật lý gồm:**
    - **Khối lượng xe đẩy.**
    - **Khối lượng cột.**
    - **Chiều dài cột.**
    - **Gia tốc trọng trường.**

## CartPole enviroment in OpenAI Gym

Để làm việc với môi trường này trong OpenAI Gym cần:

- **Cài đặt thư viện của OpenAI Gym.**
- **Tạo môi trường.**
- **Mô phỏng môi trường.**

## Popular Reinforcement Learning Algorithms for CartPole

- **Q-learning: thuật toán cơ bản với bảng tra cứu Q-value.**
- **Deep Q-learning (DQN): Sử dụng mạng neural để xấp xỉ Q-value.**
- **Policy Gradient: Tối ưu trực tiếp chính sách (policy) thay vì Q-value.**
- **Actor-Critic: Kết hợp cả hai phương  pháp Q-learning và Policy Gradient.**