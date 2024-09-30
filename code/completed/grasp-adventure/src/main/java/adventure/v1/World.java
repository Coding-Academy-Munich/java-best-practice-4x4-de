package adventure.v1;

import java.util.HashMap;
import java.util.Map;

public class World {
    private final Map<String, Location> locations;
    private final String initialLocationName;

    public World(Map<String, Location> locations, String initialLocationName) {
        this.locations = new HashMap<>(locations);
        this.initialLocationName = initialLocationName;
    }

    public Map<String, Location> getLocations() {
        return locations;
    }

    public Location getLocationByName(String name) {
        return locations.get(name);
    }

    public String getInitialLocationName() {
        return initialLocationName;
    }

    @Override
    public String toString() {
        return "World{" +
                "locations=" + locations +
                ", initialLocationName='" + initialLocationName + '\'' +
                '}';
    }
}
