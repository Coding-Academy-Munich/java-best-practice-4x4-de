package adventure.v1;

import java.util.HashMap;
import java.util.Map;

public record World(Map<String, Location> locations, String initialLocationName) {
    public World(Map<String, Location> locations, String initialLocationName) {
        this.locations = new HashMap<>(locations);
        this.initialLocationName = initialLocationName;
    }

    @Override
    public String toString() {
        return "World{" + "locations=" + locations + ", initialLocationName='" + initialLocationName + '\'' + '}';
    }
}
