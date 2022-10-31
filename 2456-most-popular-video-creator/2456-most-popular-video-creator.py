from collections import defaultdict


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creators_count = defaultdict(int)
        top_creators_video = {}
        top_creators = set()
        max_views = 0
        
        for i in range(len(creators)):
            current_creator, current_video, current_views = creators[i], ids[i], views[i]
            
            if current_creator in top_creators_video:
                top_video, top_views = top_creators_video[current_creator]
                if current_views > top_views:
                    top_creators_video[current_creator] = (current_video, current_views)
                elif current_views == top_views:
                    top_creators_video[current_creator] = (min(top_video, current_video), current_views)
            else:
                top_creators_video[current_creator] = (current_video, current_views)
            
            
            creators_count[current_creator] += current_views
            if creators_count[current_creator] == max_views:
                top_creators.add(current_creator)
                max_views = creators_count[current_creator]
            elif creators_count[current_creator] > max_views:
                top_creators = set([current_creator])
                max_views = creators_count[current_creator]
        
        return [[creator, top_creators_video[creator][0]] for creator in top_creators]