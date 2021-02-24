def find_dif_btwn_times(a, b):
    time_a = a
    time_b = b
    (h_a, m_a) = time_a.split(':')

    (h_b, m_b) = time_b.split(':')

    

    print(h_a, m_a, h_b, m_b )

find_dif_btwn_times('12:30', '10:00')