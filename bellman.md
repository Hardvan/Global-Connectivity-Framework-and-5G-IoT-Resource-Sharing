# Bellman Ford for QUEST Region

Source Node: Islamabad (Node ID: 7)

No. of Nodes: 7

## Adjacency Lists

### Peshawar Node

<table>
<tr>
  <th>Neighbour Name</th>
  <td>Karachi</td>
  <td>Faisalabad</td>
  <td>Quetta</td>
  <td>Lahore</td>
  <td>Abbottabad</td>
  <td>Islamabad</td>
</tr>
<tr>
  <th>Latency (ms)</th>
  <td>6.8</td>
  <td>2.95</td>
  <td>3.01</td>
  <td>3.49</td>
  <td>0.94</td>
  <td>1.07</td>
</tr>
</table>

### Karachi Node

<table>
<tr>
  <th>Neighbour Name</th>
  <td>Peshawar</td>
  <td>Faisalabad</td>
  <td>Quetta</td>
  <td>Lahore</td>
  <td>Abbottabad</td>
  <td>Islamabad</td>
</tr>
<tr>
  <th>Latency (ms)</th>
  <td>6.8</td>
  <td>4.93</td>
  <td>4.46</td>
  <td>5.24</td>
  <td>6.81</td>
  <td>6.5</td>
</tr>
</table>

### Faisalabad Node

<table>
<tr>
  <th>Neighbour Name</th>
  <td>Peshawar</td>
  <td>Karachi</td>
  <td>Quetta</td>
  <td>Lahore</td>
  <td>Abbottabad</td>
  <td>Islamabad</td>
</tr>
<tr>
  <th>Latency (ms)</th>
  <td>2.95</td>
  <td>4.93</td>
  <td>3.42</td>
  <td>0.74</td>
  <td>2.41</td>
  <td>2.08</td>
</tr>
</table>

### Quetta Node

<table>
<tr>
  <th>Neighbour Name</th>
  <td>Peshawar</td>
  <td>Karachi</td>
  <td>Faisalabad</td>
  <td>Lahore</td>
  <td>Abbottabad</td>
  <td>Islamabad</td>
</tr>
<tr>
  <th>Latency (ms)</th>
  <td>3.01</td>
  <td>4.46</td>
  <td>3.42</td>
  <td>4.15</td>
  <td>3.53</td>
  <td>3.35</td>
</tr>
</table>

### Lahore Node

<table>
<tr>
  <th>Neighbour Name</th>
  <td>Peshawar</td>
  <td>Karachi</td>
  <td>Faisalabad</td>
  <td>Quetta</td>
  <td>Abbottabad</td>
  <td>Islamabad</td>
</tr>
<tr>
  <th>Latency (ms)</th>
  <td>3.49</td>
  <td>5.24</td>
  <td>0.74</td>
  <td>4.15</td>
  <td>2.8</td>
  <td>2.51</td>
</tr>
</table>

### Abbottabad Node

<table>
<tr>
  <th>Neighbour Name</th>
  <td>Peshawar</td>
  <td>Karachi</td>
  <td>Faisalabad</td>
  <td>Quetta</td>
  <td>Lahore</td>
  <td>Islamabad</td>
</tr>
<tr>
  <th>Latency (ms)</th>
  <td>0.94</td>
  <td>6.81</td>
  <td>2.41</td>
  <td>3.53</td>
  <td>2.8</td>
  <td>0.34</td>
</tr>
</table>

### Islamabad Node

<table>
<tr>
  <th>Neighbour Name</th>
  <td>Peshawar</td>
  <td>Karachi</td>
  <td>Faisalabad</td>
  <td>Quetta</td>
  <td>Lahore</td>
  <td>Abbottabad</td>
</tr>
<tr>
  <th>Latency (ms)</th>
  <td>1.07</td>
  <td>6.5</td>
  <td>2.08</td>
  <td>3.35</td>
  <td>2.51</td>
  <td>0.34</td>
</tr>
</table>

## Adjacency List for Source Node: 'Islamabad' after converting ~ 50% of latencies to a large number

| Neighbour Name | Latency (ms) |
| --- | --- |
| Peshawar | 30843.04 |
| Karachi | 6.5 |
| Faisalabad | 89834.82 |
| Quetta | 67330.04 |
| Lahore | 47627.54 |
| Abbottabad | 0.34 |

## Shortest Path from Source Node to all Nodes
| Node Name | Old Distance (ms) | New Distance (ms) | Path |
| --- | --- | --- | --- |
| Peshawar | 30843.04 | 1.28 | Abbottabad -> Peshawar |
| Karachi | 6.5 | 6.5 | Karachi |
| Faisalabad | 89834.82 | 2.75 | Abbottabad -> Faisalabad |
| Quetta | 67330.04 | 3.87 | Abbottabad -> Quetta |
| Lahore | 47627.54 | 3.14 | Abbottabad -> Lahore |
| Abbottabad | 0.34 | 0.34 | Abbottabad |
| Islamabad | 0 | 0 |  |
