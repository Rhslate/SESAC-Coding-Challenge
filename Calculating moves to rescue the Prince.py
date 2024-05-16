# Bot saves Princess
# bot = m, Princess = p
# bot is in center of grid

#grid = []


while m_pos != p_pos:
    if m_pos[0] < p_pos[0]:
       moves.append("UP")
       m_pos = (m_pos[0] +1, m_pos[1])
\n

    elif m_pos[0] > p_pos[0]:
         moves.append("DOWN")
         m_pos = (m_pos[0] -1, m_pos[1])

\n

    if m_pos[1] < p_pos[1]:
       moves.append("LEFT")
       m_pos = (m_pos[0], bot_pos[1] +1)
        
\n

    elif m_pos[1] > p_pos[1]:
         moves.append("RIGHT")
         m_pos = (m_pos[1], bot_pos[1] -1)
        
        
print displayPathtoPrincess
