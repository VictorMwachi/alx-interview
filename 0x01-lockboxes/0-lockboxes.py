def canUnlockAll(boxes):
    num = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        box_index = unseen_boxes.pop()
        if not box_index or box_index >= l or box_index < 0:
            continue
        if box_index not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box_index])
            seen_boxes.add(box_index)
    return l == len(seen_boxes)
