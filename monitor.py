import scapy.all as scapy
import numpy as np
from sklearn.ensemble import IsolationForest

class PacketMonitor:
    def __init__(self):
        self.packets = []
        self.model = IsolationForest()  # Machine Learning model for anomaly detection

    def capture_packets(self):
        print('Starting packet capture...')
        scapy.sniff(prn=self.process_packet, store=False)

    def process_packet(self, packet):
        self.packets.append(packet)
        print(f'Packet captured: {packet.summary()}')
        self.analyze_traffic()

    def analyze_traffic(self):
        if len(self.packets) < 100:
            return
        traffic_data = np.array([[pkt[scapy.IP].src, pkt[scapy.IP].dst] for pkt in self.packets[-100:] if scapy.IP in pkt]).astype(str)
        anomalies = self.detect_anomalies(traffic_data)
        if anomalies.size > 0:
            self.alert_threat(anomalies)

    def detect_anomalies(self, traffic_data):
        self.model.fit(np.arange(0, len(traffic_data)).reshape(-1, 1))
        predictions = self.model.predict(np.arange(0, len(traffic_data)).reshape(-1, 1))
        return traffic_data[predictions == -1]  # Getting anomalies

    def alert_threat(self, anomalies):
        print('Threat detected! Anomalies found:')
        print(anomalies)

if __name__ == '__main__':
    monitor = PacketMonitor()
    monitor.capture_packets()