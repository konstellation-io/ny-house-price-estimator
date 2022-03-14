export const toCategory = (value: number) => {
  switch (true) {
    case value >= 10 && value <= 90:
      return "low";
    case value > 90 && value <= 180:
      return "mid";
    case value > 180 && value <= 400:
      return "high";
    case value > 400:
      return "lux";
  }
};

export const getCategoryValues = (category: string) => {
  switch (category) {
    case "low":
      return "10-90";
    case "mid":
      return "90-100";
    case "high":
      return "180-400";
    case "lux":
      return "+400";
  }
};
