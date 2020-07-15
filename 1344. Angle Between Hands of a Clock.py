class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour%12
        h_angle = (hour + minutes/60)*(360/12)
        m_angle = minutes*(6)
        
        return min(abs(h_angle-m_angle),360-abs(h_angle-m_angle))